// Create a function getStudentsByLocation that returns an array of objects who are located in
// a specific city.
// It should accept a list of students (from getListStudents) and a city (string) as parameters.
// You must use the filter function on the array.

function getStudentsByLocation(array, city) {
// function that takes in an array and a city
  return array.filter((item) => item.location === city);
} // return array of objects who are located in a specific city

export default getStudentsByLocation;
