// Create a function getStudentIdsSum that returns the sum of all the student ids.
// It should accept a list of students (from getListStudents) as a parameter.
// You must use the reduce function on the array.

import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(students) {
  // function that takes in an array of students and returns an array of their ids
  const ids = getListStudentIds(students);
  // const ids = array.map((item) => item.id);
  // array of student ids from the array of students
  return ids.reduce((a, b) => a + b);
  // returns the sum of all the student ids in the array
  // a is the accumulator, b is the current value
}
