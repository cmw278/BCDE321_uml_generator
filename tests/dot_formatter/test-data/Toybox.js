class Toybox {
  constructor () {
    this.allMyToys = []
  }

  addToy (newName, newColour, newCost) {
    this.allMyToys.push(new Toy(newName, newColour, newCost))
  }

  getToyCount () {
    return this.allMyToys.length
  }

  toString () {
    toyboxString = `The toybox has ${this.getToyCount()} toys.`
    for (const aToy of this.allMyToys) {
      toyboxString += `\n\t${aToy.toString()}`
    }
    return toyboxString
  }
}