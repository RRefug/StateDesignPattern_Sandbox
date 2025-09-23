# State Design Pattern Deeper Dive Exploration

<img width="463" height="427" alt="state" src="https://github.com/user-attachments/assets/2be95755-dd5e-4741-a269-b71faa90807b" />


Intrigued with clean code, refactoring, system design, and code architecture. I remembered design patterns and was hoping to use some in an ongoing project. Eager to deepen my understanding, I started exploring the **State Design Pattern** through a small work-in-progress project.

I used online resources to guide my initial outline and built the project based on pseudocode examples. Along the way, I improved my ability to read UML class diagrams and interpret relationships like aggregation and association — skills that will definitely help me implement other patterns in future projects, including my ongoing **Alien Invasion** refactor. 

<img width="773" height="550" alt="stateDesignPattern" src="https://github.com/user-attachments/assets/f483e9a6-d9df-4e9a-8a4e-a206b025c904" />

<img width="821" height="633" alt="abstractclassandinterfaceclass" src="https://github.com/user-attachments/assets/f138a1c8-60e2-45ec-b7b0-4f776695b638" />
<img width="477" height="446" alt="image" src="https://github.com/user-attachments/assets/116cd16f-02de-4e3c-aa6f-58c8b699c031" />
<img width="477" height="346" alt="statepseudocode" src="https://github.com/user-attachments/assets/71b709ce-dcd6-4db3-a4e4-7df22a45a0d7" />




This repo is a sandbox for experimenting with architectural ideas with the State Design Pattern. Right now, I'm tackling a circular import issue and working toward a cleaner package structure using `__init__.py` files to expose interfaces. I got this state design pattern working! Not the way I intended to originally. I've learned that there will be times when it's good to keep certain classes together in one module rather than many when they rely strongly on one another. 

" The only time I think it's correct to use more than one class per file is when you are using internal classes... but internal classes are inside another class, and thus can be left inside the same file. The inner classes roles are strongly related to the outer classes, so placing them in the same file is fine."
     - Quote from https://stackoverflow.com/questions/360643/is-it-a-bad-practice-to-have-multiple-classes-in-the-same-file

I tried to separate one module because it had more than one class within it. However, it led to my issue with circular imports for a couple days. Circular imports happen when two, or more, different modules try to import the classes stored within themselves before the entire module can finish initializing (Ex: ClassA tries to import ClassB while ClassB is importing ClassA).

Circular imports also means 'smelly code' and despite me following multiple pseudocodes from the internet, it always led to a circular import issue. Preventing me from even getting past the first step. To my discovery, Python worries about circular imports more than other programming languages. However, I found a pseudocode that works and I was able to trace the code, see what was underneathe the hood, and follow it from start to finish. If you want to run it for yourself, visit the site Refacturing Guru and look at the python example. Link: https://refactoring.guru/design-patterns/state/python/example#lang-features
Or see my detailed explanation within state_pkg. Run the main.py module and bam! Works.

Besides that, I have also remembered, but totally forgot, that it is 100% okay to know when you should try aa different approach. That is what happened with main_pkg. That was the original pseudocode I tried following, but then led to me following another pseudocode, both suffering from the circular import issue. However, a glimmer of hope finally hit and I found a working example. Learned a lot from it and about python. This sandbox became a smaller project on its own. HOLY COW!!! Feels good that I didn't give up. I'm making the time to learn and I am very proud of this small step forward with A LOT of knowledge under my belt. 

Now that I am finished with this state design pattern, I have learned a lot more than I thought I would and ready to carry on with my bigger project, Alien Invasion, but refactored into a more efficient and tested version. This is definitely going to make other design patterns and cleaner code a breeze. 


What I got out of this: 
- Understand and implement the State Design Pattern
- Practice reading and applying UML diagrams
- Explore package structure and import management in Python
- Apply lessons learned to larger projects like Alien Invasion


helpful design pattern website: https://refactoring.guru/design-patterns/state  
helpful UML class diagram associations website: https://creately.com/guides/class-diagram-relationships/  

NOTE: These pictures are screenshots belonging to their respectful websites (Thank you!)
