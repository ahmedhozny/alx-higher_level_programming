#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  let num1 = Math.max(arr[0], arr[1]);
  let num2 = Math.min(arr[0], arr[1]);
  for (let i = 2; i < arr.length; i++)
    if (arr[i] > num1) {
      num2 = num1;
      num1 = arr[i]
    } else if (arr[i] > num2) {
      num2 = arr[i]
    }
  console.log(num2);
}
