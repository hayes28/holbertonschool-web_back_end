// Implement a class named Currency:
// - Constructor attributes:
// code (String)
// name (String)
// Each attribute must be stored
// in an “underscore” attribute
// version (ex: name is stored in _name)
// Implement a getter and setter for each attribute.
// Implement a method named displayFullCurrency that
// will return the attributes in the following format name (code).

export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw TypeError('Code must be a string');
    }
    this._code = newCode;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = newName;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
