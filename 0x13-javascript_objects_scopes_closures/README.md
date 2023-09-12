# JavaScript - Objects, Scopes and Closures

["JavaScript - Objects, Scopes, and Closures"]() is a broad topic that encompasses several important aspects of the JavaScript programming language.

[Let's break down these concepts:]()

1. ***Objects:*** In JavaScript, objects are a fundamental data type. They are used to group related data and functions together. Objects can have properties (data) and methods (functions). Objects can be created using object literals or by defining constructor functions.

Example of an object literal:

```
const person = {
  name: 'John',
  age: 30,
  sayHello: function() {
    console.log(`Hello, my name is ${this.name}.`);
  }
};
```


2. ***Scopes:*** JavaScript has function-level scope. Variables declared inside a function are only accessible within that function (local scope). Variables declared outside of any function are in the global scope and can be accessed throughout the program. There's also block-level scope introduced with the let and const keywords in modern JavaScript.

Example of scope:

```
let globalVar = 'I am global';

function foo() {
  let localVar = 'I am local';
  console.log(globalVar); // Accessible
  console.log(localVar);  // Accessible
}
```

3. ***Closures:*** Closures are a powerful and somewhat advanced concept in JavaScript. A closure is a function that has access to variables from its outer (enclosing) function, even after the outer function has finished executing. Closures are often used to create private variables and encapsulate behavior.
Example of a closure:

```
function outer() {
  let outerVar = 'I am from outer';
  
  function inner() {
    console.log(outerVar); // Accessing outerVar from the enclosing scope
  }

  return inner;
}

const innerFunc = outer();
innerFunc(); // Prints "I am from outer"
```

[Note That:]() These concepts are foundational to understanding JavaScript and are crucial for effective programming in the language. Objects are used to organize and manipulate data, scopes determine variable accessibility and lifetime, and closures enable advanced patterns like encapsulation and data hiding.


## REVIEW QUESTIONS

1. ***JavaScript is considered amazing for various reasons:***

* **Versatility**: JavaScript is a versatile language that can be used for both front-end and back-end web development. It can also be used for mobile app development (e.g., with frameworks like React Native) and even serverless computing.

* **Widespread Adoption:** It is one of the most widely used programming languages, making it an essential skill for web developers. JavaScript runs in all modern browsers, ensuring broad compatibility.

* **Community and Ecosystem:** JavaScript has a large and active developer community. This has led to a vast ecosystem of libraries and frameworks (e.g., React, Angular, Vue.js, Node.js) that simplify development.

* **Asynchronous Programming:** JavaScript's event-driven, non-blocking nature is excellent for handling asynchronous tasks. This is crucial for modern web applications where many operations happen concurrently.

* **Object-Oriented:** JavaScript supports object-oriented programming (OOP), enabling the creation of reusable and structured code using objects and prototypes.


2. ***How to create an object in JavaScript:*** Objects in JavaScript can be created using object literals or constructor functions. For example:

```
const person = {
  name: 'John',
  age: 30
};
```


3. ***What "this" means:*** In JavaScript, this refers to the current execution context. Its value depends on how a function is called. Inside an object method, `this` refers to the object itself.


4. ***What undefined means:*** undefined is a special value in JavaScript that represents the absence of a value. It is often used for uninitialized variables or when a value is not returned from a function.


5. ***Why variable type and scope are important:*** Variable type (data type) and scope (where a variable is accessible) are essential for writing bug-free and maintainable code. Understanding these concepts helps prevent unexpected behaviors and improves code organization.


6. ***What is a closure:*** A closure is a function that has access to the variables from its outer (enclosing) function, even after the outer function has finished executing. Closures are used for encapsulation and data hiding.


7. ***What is a prototype:*** In JavaScript, every object has a prototype, which is an object from which it inherits properties and methods. Prototypes enable inheritance and help create efficient object relationships.


8. ***How to inherit an object from another:*** In JavaScript, object inheritance is achieved through prototypes. You can create a child object that inherits properties and methods from a parent object using the Object.create() method or by using constructor functions and the prototype property.

* Example using Object.create():

```
const parent = { x: 10 };
const child = Object.create(parent);
child.y = 20;
```

* Example using constructor functions:

```
function Parent() {
  this.x = 10;
}

function Child() {
  this.y = 20;
}

Child.prototype = new Parent();
const child = new Child();
```

=> The child object (child) inherits properties from the parent object (parent) in both examples.
