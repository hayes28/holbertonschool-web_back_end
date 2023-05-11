// Using the prototype below, return a promise. The parameter is a boolean.
// getFullResponseFromAPI(success)
// If success is true, return resolve({ status: 200, body: 'Success' })
// Otherwise, return reject(Error('The fake API is not working currently'))

export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ status: 200, body: 'Success' });
    } else {
      reject(Error('The fake API is not working currently'));
    }
  });
}
