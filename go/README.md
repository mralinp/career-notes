# Go
Go, often referred to as Golang, is a statically typed, compiled programming language designed by Google. It was created by Robert Griesemer, Rob Pike, and Ken Thompson and was first released in 2009.

Go is known for its simplicity, efficiency, and scalability, making it particularly well-suited for building large-scale, concurrent systems. It incorporates features such as garbage collection, static typing, memory safety, and CSP-style concurrency, which makes it easier to write efficient and robust code for distributed systems and cloud computing.

Some key features of Go include:

- **Concurrency**: Goroutines and channels provide built-in support for concurrent programming, making it easy to write programs that efficiently utilize multiple cores.

- **Garbage Collection**: Go includes a garbage collector that automatically manages memory allocation and deallocation, reducing the burden on developers for memory management.

- **Static Typing**: Go is statically typed, which means variable types are checked at compile-time, reducing runtime errors.

- **Simplicity**: Go's syntax is simple and easy to understand, which makes it accessible to new developers and helps maintain code readability.

- **Performance**: Go compiles directly to machine code, resulting in high performance. It is often used in performance-critical applications where speed is important.

- **Cross-platform**: Go programs can be compiled to run on various operating systems, including Linux, macOS, and Windows, making it a versatile language for developing applications across different platforms.

Overall, Go is widely used in various domains, including web development, cloud services, network programming, and system programming, and it continues to gain popularity due to its simplicity, performance, and concurrency support.
## Installation
To install go, visit the official website, download the installer package and install it on your computer. After installing go, don't forget to add go path to the `$PATH` environment variable of your computer.
## Hello, Go!

To get started learning go, we have to first make a directory, inside the directory we need to create a `go.mod`, module file, and `main.go` which is where we write our codes.

```console
$ mkdir go-tutorial && cd go-tutorial
$ go mod init go-tutorial/main
$ touch main.go
```

then write the simple hello world program inside of `main.go` file and save the changes.

```go
// The package name which should be exists at the top of each file we create
// Note: package main means that our code should be compiled to an executable
package main

// importing the required io package which contains the 'Println' function
import "fmt"

// function main shouldn't return any thing and doesn't get any parameters
func main() {
    fmt.Println("Hello, Go!")
}
```

Running go program is simple, just type `go run .` and if you want to compile your code write the command `go build .`.

```console
$ go run .
```
## Variables

In Go, there are several types of variables, each with its own characteristics. Here's a brief overview:

- **Primitive Types**: These are the basic data types built into the language.
  - Numeric Types: int, uint, float32, float64, etc.
  - String Type: string
  - Boolean Type: bool
  - Complex Types: complex64, complex128
  - Byte Type: byte (alias for uint8)
  - Rune Type: rune (alias for int32)

- **Composite Types**: These are types that can hold multiple values.
  - Array: var arr [5]int (fixed-size sequence of elements)
  - Slice: var slice []int (dynamic-size sequence built on top of arrays)
  - Map: var m map[string]int (unordered collection of key-value pairs)
  - Struct: type Person struct { Name string; Age int } (composite type that groups together variables)

- **Pointer Types**: These hold memory addresses of variables.
  - var ptr *int (pointer to an integer)
  - var ptr *Person (pointer to a struct)

- **Function Types**: These represent functions.
  - var fn func(int) int (function that takes an integer argument and returns an integer)

- **Interface Types**: These define a set of methods.
  - type Reader interface { Read(p []byte) (n int, err error) }

- **Channel Types**: These facilitate communication between goroutines.
  - var ch chan int (channel that carries integers)

- **Other Types**: There are additional types such as error, interface{}, and custom types defined by users.

In addition to these types, Go also supports **constants** and **variables** declared with the `var` keyword. Variables can be declared at package, function, or block scope, and they can be initialized with values or left uninitialized (in which case they are given a zero value according to their type).

## Functions

In Go, functions are defined using the func keyword followed by the function name, parameters (if any), return type (if any), and the function body enclosed in curly braces. Here's the basic syntax:

```go
func functionName(parameters) returnType {
    // function body
}
```

Let's break down the parts of a function declaration:

- func: This keyword is used to declare a function.
- functionName: This is the name of the function.
- parameters: These are optional, and they specify the inputs to the function. Parameters are a comma-separated list of name type pairs. If a function doesn't take any parameters, this part can be omitted.
- returnType: This is optional as well. It specifies the type of the value(s) returned by the function. If a function doesn't return anything, this part can be omitted.
- function body: This contains the statements that define what the function does. It's enclosed in curly braces {}.

Here's an example of a simple function that takes two integers and returns their sum:

```go
func add(x, y int) int {
    return x + y
}
```

Functions in Go can also return multiple values:

```go
func divide(dividend, divisor int) (int, error) {
    if divisor == 0 {
        return 0, errors.New("division by zero")
    }
    return dividend / divisor, nil
}
```

You can call functions like this:

```go
result := add(3, 5)
fmt.Println(result) // Outputs: 8

result, err := divide(10, 2)
fmt.Println(result, err) // Outputs: 5 <nil>

result, err = divide(10, 0)
fmt.Println(result, err) // Outputs: 0 division by zero
``` 

Functions are first-class citizens in Go, meaning you can assign them to variables, pass them as arguments to other functions, and return them from other functions. This flexibility enables powerful functional programming techniques.

## Structs

In Go, a struct is a composite data type that groups together variables of different types under a single name. It's similar to a class in object-oriented programming languages, but without methods attached to it. Here's the basic syntax for defining a struct:

```go
type StructName struct {
    field1 type1
    field2 type2
    // more fields...
}
```

Where:

- `StructName` is the name of the struct.
- `field1`, `field2`, etc., are the names of the fields (also called members or properties).
- `type1`, `type2`, etc., are the types of the fields.

For example, let's define a `Person` struct with `name`, `age`, and `city` fields:

```go
type Person struct {
    name string
    age  int
    city string
}
```

You can create instances of a struct using the struct literal syntax:

```go
person1 := Person{name: "Alice", age: 30, city: "New York"}
person2 := Person{"Bob", 25, "Los Angeles"}
const person3 = Person{"Ali", 27, "Tehran"}
```

You can access and modify struct fields using dot notation:

```go
fmt.Println(person1.name) // Outputs: Alice
fmt.Println(person2.city) // Outputs: Los Angeles

person1.age = 31
fmt.Println(person1.age) // Outputs: 31
```

Structs in Go are value types, meaning when you assign a struct to another variable or pass it as an argument to a function, **a copy of the struct is made**. **This contrasts with slices and maps, which are reference types**.

Structs are commonly used to represent real-world entities and data structures in Go programs. They provide a convenient way to organize related data and pass it around as a single unit.

## 
