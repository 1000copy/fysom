// Here's the function that we want to recurse.
X = function (recurse, n) {
  if (0 == n)
    return 1;
  else
    return n * recurse(recurse, n - 1);
};

// This will get X to recurse.
Y = function (builder, n) {
  return builder(builder, n);
};

// Here it is in action.
var a =Y(
  X,
  5
);
console.log(a)
a =Y(
  X,
  1
);


console.log(a)