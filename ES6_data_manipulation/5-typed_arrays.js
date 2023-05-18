// Create a function named createInt8TypedArray that returns a new
// ArrayBuffer with an Int8 value at a specific position.
// It should accept three arguments: length (Number), position (Number), and value (Number).
// If adding the value is not possible the error Position outside range should be thrown.

export default function createInt8TypedArray(length, position, value) {
  // Create a new ArrayBuffer with the length passed as argument
  // to the function createInt8TypedArray
  const buffer = new ArrayBuffer(length);
  // Create a new DataView of the ArrayBuffer
  const view = new DataView(buffer);
  // If adding the value is not possible the error Position outside range should be thrown.
  if (position >= length) {
    throw new Error('Position outside range');
  }
  view.setInt8(position, value); // Set the value at the position passed
  // as argument to the function createInt8TypedArray
  return view;
}
