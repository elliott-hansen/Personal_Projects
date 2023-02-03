// Pandigital - - - Elliott Hansen 11-02-2022

function Pandigital(int){
  // Approach: create a set of all the digits (0-9) and remove them as they are found within the integer. Check the contents of the set at the end.
  // Edge case check (not a number, not an integer, no input)
  if((typeof(int) !== 'number' && (int % 1 !== 0)) || int.length === 0)
  {
    console.log('A valid input was not provided.');
    return;
  }
  // Construct set of digits
  const digits = new Set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']);
  int = int.toString().split('');
  for(i = 0; i < int.length; i++) {
    // If int is already determined to be pandigital, break
    if(digits.size === 0){
        break;
    }
    if(digits.has(int[i])) {
      console.log(int[i]+' is a digit in the integer')
      // Remove found digit from set
      digits.delete(int[i])
      console.log(digits)
    }
  }
  // If there were unfound digits remaining, not pandigital
  if(digits.size > 0) {
    console.log('\nInteger is not pandigital.')
    return;
  }
  // Otherwise, it is!
  else {
    console.log('\nInteger is pandigital!')
    return;
  }
}
// UNCOMMENT FOR USE IN BROWSER
// CheckPalindrome(prompt('Enter a word: '))

// UNCOMMENT FOR USE IN NODE
const readline = require('readline').createInterface( {input: process.stdin, output: process.stdout} );
readline.question('Enter an integer: ', inp => { Pandigital(inp); readline.close();} )