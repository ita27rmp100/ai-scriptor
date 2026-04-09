vascriptconst readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

let num1, num2, operation;

readline.question('Enter the first number: ', (n1) => {
  num1 = parseFloat(n1);
  readline.question('Enter the second number: ', (n2) => {
    num2 = parseFloat(n2);
    readline.question('Enter the operation (+, -, *, /): ', (op) => {
      operation = op;
      let result;
      switch (operation) {
        case '+':
          result = num1 + num2;
          break;
        case '-':
          result = num1 - num2;
          break;
        case '*':
          result = num1 * num2;
          break;
        case '/':
          if (num2 !== 0) {
            result = num1 / num2;
          } else {
            result = 'Error: Division by zero';
          }
          break;
        default:
          result = 'Error: Invalid operation';
      }
      console.log(`Result: ${result}`);
      readline.close();
    });
  });
});
