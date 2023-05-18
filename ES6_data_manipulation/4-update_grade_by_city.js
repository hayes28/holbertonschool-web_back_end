// Create a function updateStudentGradeByCity that returns an array of
// students for a specific city with their new grade
// It should accept a list of students (from getListStudents), a city (String),
// and newGrades (Array of “grade” objects) as parameters.
// newGrades is an array of objects with this format: { studentId: 31, grade: 78 }

export default function updateStudentGradeByCity(students, city, newGrades) {
  // function that takes in a list of students, a city, and new grades
  const studentsByCity = students.filter((item) => item.location === city);
  // const studentsByCity = students.filter((item) => item.location.localeCompare(city) === 0);
  // array of students filtered by city
  const studentsById = studentsByCity.map((item) => item.id);
  // array of student ids filtered by city
  const studentsWithGrades = studentsById.map((id) => {
    const student = students.find((item) => item.id === id);
    const grade = newGrades.find((item) => item.studentId === id);
    return { ...student, grade: grade ? grade.grade : 'N/A' };
  });
    // array of students with their grades
  return studentsWithGrades;
  // returns the array of students with their grades
}
