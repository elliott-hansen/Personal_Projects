// Palindrome - - - Elliott Hansen 11-02-2022

function CheckPalindrome(input) {
  // Approach: convert the input to an array and track the start index (0) and end index (inp.length-1). Move them towards the middle and compare.
  // Check for a valid input (i.e: not nothing)
  if(input.length === 0) {
    console.log('A valid input was not provided.')
    return;
  }
  // Trivial/base case 
  else if(input.length === 1) {
    console.log('Input is one character long. Trivially, it is a palindrome.');
    return;
  }
  // Remove spaces, account for capitalization.
  input = input.split(' ').join('').toLowerCase()
  let i = 0;
  let j = input.length - 1;
  console.log('Start index: ' + i + ' End index: ' + j + '\n');
  input = input.split('');
  // Character in the middle of odd-length inputs will not matter, trivial case.
  while(i < j) {
    console.log('Checking if: ' + input[i] + ' is the same as ' + input[j]);
    if(input[i] !== input[j]) {
      console.log('\nInput is not a palindrome.');
      return;
    }
    else {
      i = i + 1;
      j = j - 1;
    }
  }
  console.log('\nInput is a palindome.');
  return;
}
// UNCOMMENT FOR USE IN BROWSER
// CheckPalindrome(prompt('Enter a word: '))

// UNCOMMENT FOR USE IN NODE
// const readline = require('readline').createInterface( {input: process.stdin, output: process.stdout} );
// readline.question('Enter a word, phrase, or input: ', inp => { CheckPalindrome(inp); readline.close();} )