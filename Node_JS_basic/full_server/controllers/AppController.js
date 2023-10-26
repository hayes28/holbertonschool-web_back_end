// 8. Organize a complex HTTP server using Express
// 8.2 Write the App controller
// Create a class named AppController. Add a static method named getHomepage

class AppController {
  static getHomepage(req, res) {
    res.status(200).send('Hello Holberton School!');
  }
}

module.exports = AppController;
