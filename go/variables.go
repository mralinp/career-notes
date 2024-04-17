package main

import "fmt"


func Variables() string {
	// constant
	const pi = 3.14159

	// multiple constants
	const (
		beta = 10
		sigma = .2
		gamma = 13
		productName = "tutorial"
	)
	
	// common variables
	var booleanVariable bool = true
	var stringVariable string = "hello"
	var charVariable char = 'c'
	var integerVariable int32 = 1230
	var floatVariable float32 = 1234.2345
	
	// multiple variables

	var (
		userName = "Ali"
		country = "Iran"
	)

	// defining without var keyword
	myName := "ali_nader"
	
	// arrays
	var numbers = [5]int{1,2,3,4,5}
	var names = [...]string{"ali", "ehsan", "mamad"}
	
	return fmt.Sprintf(
		"boolean: %v\nstring: %s\ninteger: %d\nfloat: %f\nmy_name: %s\npi: %f", 
		booleanVariable, 
		stringVariable, 
		integerVariable, 
		floatVariable,
		myName,
		pi,
	)
}