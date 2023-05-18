// Create a function named cleanSet that returns
// a string of all the set values that start with
// a specific string (startString).
// It accepts two arguments: a set (Set) and a startString (String).
// When a value starts with startString you only append the rest of
// the string. The string contains all the values of the set separated by -.

export default function cleanSet(set, startString) {
  // Check if the set is an instance of Set
  if (!startString || !startString.length) {
    return '';
  }
  const result = [];
  // Iterate through the set
  set.forEach((item) => {
    // Check if the item starts with startString
    if (item && item.startsWith(startString)) {
      // If it does, append the rest of the string
      result.push(item.slice(startString.length));
    }
  });
  return result.join('-');
}
