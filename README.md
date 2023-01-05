# A simple quantum circuit simulator

This is a fairly minimal codebase for simulating quantum circuits. It is intended for my own professional use only, though I suspect others will also find it useful and so I am making the repository public. Comments, bug reports, and pull requests are welcome.

## Purpose

I intend to use this codebase for the following purposes.

1. **Research.**
I have become reasonably well known in the quantum computing community for commentary [like this](https://www.youtube.com/watch?v=qYuxOx4Z8Yk). Though no one has said it to me directly, I assume there are plenty of people out there who think I should put up or shut up about how quantum computer programming is supposed to work. This codebase is a testbed for a small but important part of my answer. Read on to find out how.

2. **Teaching.**
I expect to be teaching quantum programming to others over the course of my career. Reference code is invaluable for such teaching and so I intend for this codebase to be that reference.

3. **Validation of simple circuits.**
I have frequently found it useful to simulate simple quantum circuits in order to test new ideas. After years of this kind of work, I have found myself repeatedly writing the same or similar code, which basically involves constructing a list of matrices and multiplying them in order to a target vector. This codebase is supposed to save me from having to reinvent the wheel over and over again.

## Scope

This code is written to do exactly one thing: simulate the effect of a quantum circuit in an easily intelligible fashion. Thus the code's job is to turn a circuit (defined below) into a sequence of matrix multiplication operations.

Performance is a non-goal of this project. I am therefore using dense matrix methods in Python. Remember, the point is that the code should be *easily intelligible*. That way I can trust the output and use it to validate potentially very complex quantum circuit designs.

Noise modelling is also a non-goal of this project. This is why I have made no attempt to connect to projects like [qsim](https://github.com/quantumlib/qsim).

## Concepts

(WIP)

* **Quantum Gate.** A logic gate that acts on some number of qubits. A quantum gate is entirely specified by a matrix and a name.
* **Quantum Register.** An array of qubits upon which the quantum circuit will act.
* **Quantum Operation.** An instruction about how to apply a given quantum gate to a given quantum register. Aside from the obvious data (a quantum gate and a quantum register), a quantum operation requires *gate targets*, meaning an identification of which qubits in the register correspond to the qubits within the gate specification. A quantum operator can also take an optional argument that specifies which qubits in the register will serve as *controls* for the application of the quantum gate.
* **Quantum Circuit.** A list of quantum operations that act on a given quantum register.

## Why not use Qiskit/Q\#/Cirq/Silq/...?

**Rant incoming.**

I had hoped that such projects would eventually do something like what this codebase does, but alas no. All these projects are focussed on developing features I don't need (or particularly want), and does not develop the features I do need/want. To be upfront about this, the features I want (but am not implementing in this codebase) have to do with optimising quantum circuits by taking advantage of algebraic properties of specific gate sequences (e.g. the pairwise commutativity of single-qubit gates applied to distinct qubits) in order to simplify a given quantum circuit in terms of simulation cost. I say more about this below.

I think [Silq](https://silq.ethz.ch) is probably closest to what I want but builds certain conceptual errors deep into the language. In case anyone from that team reads this, I have two specific criticisms.

* **Silq misunderstands the model of computing underlying the concept of quantum circuits.**
This misunderstanding is encapsulated by the implementation of what Silq calls quantum control "flow". The mistake is this: whereas *classical* control flow uses the output of a Boolean function to update the instruction pointer (i.e. a machine-level conditional jump instruction), *quantum* control does no such thing. By treating classical and quantum controls on an equal footing, Silq is actually counterproductive for expressing controlled quantum operations. Quantum control should instead be treated as a block encoding (i.e. a macro that operates on a quantum circuit) that is specified by a Boolean function.

* **Uncomputation is only the simplest technique for disentangling and hence freeing quantum registers.**
The Silq team discusses uncomputation in [their paper](https://files.sri.inf.ethz.ch/website/papers/pldi20-silq.pdf) by reference to Grover search (see Sec. 4.3). But this is too simple an example to indicate how quantum registers get freed in general, as is the triangle-finding algorithm example considered in Fig. 2. Hence the main selling point of Silq – that it enables automated uncomputation – is of extremely limited benefit to me. I would actually prefer working with a language that didn't do this kind of thing automatically, because the majority of my time working with a quantum algorithm is spent ensuring safe deallocation of quantum memory.

To elaborate on safe quantum memory deallocation, I refer to [a paper](https://arxiv.org/abs/1711.10460) I worked on some years ago. That paper presents, amongst other things, two carefully worked out quantum subroutines for a task we called "antisymmetrisation". Both contain complex methods for disentangling (and hence freeing) quantum registers that are not simply uncomputations. The more complicated of the two is presented on page 2, and involves *two* disentangling steps: step 3 disentangles through the use of a cunning measurement, and step 4 disentangles by uncomputing a sort *using different quantum registers than the forward version of the sort*. An easier-to-understand algorithm is presented on page 13, and again involves two disentangling steps: steps 4 and 6. I won't go through them here (they're much easier to understand) but suffice it to say that we erased registers using techniques that were not simply uncomputations.

The point is this: a significant portion of quantum programming is spent on safely deallocating quantum registers by devising bespoke methods for ensuring those quantum registers are disentangled from any other registers that are still needed for the computation. Neither Silq nor any other quantum language offers me any help in that task. Instead, they offer features that automate what are quite frankly very naïve ideas about what quantum programmers do. By working with those languages, I have to spend most of my time actively avoiding those features and using only the core capabilities of the language, which is to express quantum circuits using an inexpressive gateset (e.g. Clifford+T). It is easier and faster for me to implement what I need from scratch. And I make the effort public in the hopes of demonstrating to quantum language designers what features I would consider beneficial and not, to put it bluntly, a major hinderance.
