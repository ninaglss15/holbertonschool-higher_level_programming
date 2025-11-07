#!/usr/bin/node

function fact (nbr) {
  nbr = parseInt(nbr);
  if (isNaN(nbr)) {
    return 1;
  } else if (nbr === 0) { return 1; } else if (nbr < 0) { return 1; }

  return nbr * fact(nbr - 1);
}
const nbr = process.argv[2];
console.log(fact(nbr));