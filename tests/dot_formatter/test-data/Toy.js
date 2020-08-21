class Toy {
  constructor (name, colour, cost) {
    this.name = name
    this.colour = colour
    this.cost = cost
  }

  toString () {
    return `${this.name} the ${this.colour} toy costed $${this.cost}.`
  }
}