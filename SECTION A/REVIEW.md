public class recursion {
 
	public static void main(String[] args) {
 
		// Saves the string that would be reversed
		String myStr = "emosewA si avaJ";
 
 
		//create Method and pass and input parameter string 
		String reversed = reverse_string(myStr);
		System.out.println("The reversed string is: " + reversed + "\nFibonacci Series of 10 numbers:0 1 1 2 3 5 8 13 21 34 ");
	

	}
 
 
	//Method take string parameter and check string is empty or not
	public static String reverse_string(String myStr)
	{
		if (myStr.isEmpty()){
		 System.out.println("String in now Empty");
		 return myStr;
		}
		//Calling Function Recursively
		System.out.println("String to be passed in Recursive Function: "+myStr.substring(1));
		return reverseString(myStr.substring(1)) + myStr.charAt(0);}

	public static <T> void function(T maxNumber) {
		// Set it to the number of elements you want in the Fibonacci Series
		int maxNumber = 10; 
		int previousNumber = 0;
		int nextNumber = 1;
		 
	    System.out.print("Fibonacci Series of "+maxNumber+" numbers:");
 
	for (int i = 1; i <= maxNumber; ++i){
	    System.out.print(previousNumber+" ");
	    // On each iteration, we are assigning second number
	    // to the first number and assigning the sum of last two
	    // numbers to the second number
	    int sum = previousNumber + nextNumber;
	    previousNumber = nextNumber;
	    nextNumber = sum;
	    }
 
	}
 
}

# Section A: Code Review - Option 2: Java Task
## Scores
* **Overall Score: 65**
* * **Correctness: 2/4**
* * **Efficiency: 3/4**
* * **Style: 3/4**
* * **Documentation: 3/4**


## Positive Aspects
Your code is well commented and it is structured neatly. You also showed good understanding of what you need to do in your first function (reverse_string),  Comments are clear at indicating what the code does.

## Aspects that could be improved
I would focus on changing your approach for the Fibonacci Series to fit with a recursive method and just fixing the few errors in your code.
Refer to the comments above on how to fix your solution.  It is much better practice to separate your 'main' method from your calculation methods in your program. Grouping similar functions together helps you to better read and control changes in your code, especially when you are dealing with large programs.
    The name, 'function' is not good naming practice. When creating a method/ function it is important not to use common programming terms, as this can be confusing to anyone reading your code. Rather go with names that describe what the method will be doing, such as 'fibonacci'.
    When programming, it is important to follow good styling practices. This allows programmers (Including yourself) to easily read and follow your code in order to work more efficiently. Remember to always indent your code correctly and to use declaritive names for your functions and variables. Always doublecheck the naming convention of your current language if you are unsure.
    
The return keyword in the 'reverse_string' function is calling a function that does not exist. This is due to naming the function incorrectly. When you call the 'reverseString' on line 26, it needs to match the same casing as the 'reverse_string' that you defined on line 18.   
The variable 'maxNumber' is being defined twice. Once in the parameter of 'function' on line 28, and then once again as an integer on line 30. This leads to runtime errors due to your computer not knowing how to define the variable.    
The 'function' method is not being called, which means the code for it is not being used at all. The print statement inside the 'main' method will need to call the 'function' method in order for it to create the Fibonacci Series.

## Overall Feedback
This is a very good attempt. Please try implementing your fibonacci function recursively and read through the Java style guide. Keep up the the good work you almost there.

