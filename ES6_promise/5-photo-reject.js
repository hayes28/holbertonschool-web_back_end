// Write and export a function named uploadPhoto. It should accept one argument fileName (string).
// The function should return a Promise rejecting with an Error
// and the string $fileName cannot be processed
// export default function uploadPhoto(filename) {}

export default function uploadPhoto(filename) {
  return Promise.reject(new Error(`${filename} cannot be processed`));
}
