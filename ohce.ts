import readline from 'readline';

// Create readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to check if a string is a palindrome
function isPalindrome(str: string): boolean {
  return str === str.split('').reverse().join('');
}

// Start the application
console.log('Bonjour');

rl.on('line', (input: string) => {
  if (input === 'exit') {
    console.log('Au revoir');
    rl.close();
  } else {
    console.log(`Mirror: ${input}`); // Mirror feature
    if (isPalindrome(input.replace(/\s+/g, '').toLowerCase())) {
      console.log('Bien dit'); // Palindrome response
    }
  }
});