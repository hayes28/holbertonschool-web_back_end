// Import the ClassRoom class from 0-classroom.js
// Implement a function named initializeRooms.
// It should return an array of 3 ClassRoom objects
// with the sizes 19, 20, and 34 (in this order).

import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const room1 = new ClassRoom(19);
  const room2 = new ClassRoom(20);
  const room3 = new ClassRoom(34);
  return [room1, room2, room3];
}
