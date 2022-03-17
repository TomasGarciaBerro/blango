function sayHello(name) {
  if (name === undefined) {
      console.log('Hello, no name')
  } else {
       console.log('Hello, ' + name)
  }
}

const name = 'Your Name'  // Put your name here

console.log('Before setTimeout')

setTimeout(() => {
    sayHello(name)
  }, 2000
)

console.log('After setTimeout')