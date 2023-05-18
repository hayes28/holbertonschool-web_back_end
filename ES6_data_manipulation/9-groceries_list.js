// Create a function named groceriesList that returns a map of groceries
// with the following items (name, quantity):
// Apples, 10 Tomatoes, 10 Pasta, 1 Rice, 1 Banana, 5

export default function groceriesList() {
  // Create a new Map
  const groceries = new Map();
  // Set the items in the Map
  groceries.set('Apples', 10);
  groceries.set('Tomatoes', 10);
  groceries.set('Pasta', 1);
  groceries.set('Rice', 1);
  groceries.set('Banana', 5);
  // Return the Map
  return groceries;
}
