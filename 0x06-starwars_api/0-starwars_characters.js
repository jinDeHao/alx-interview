#!/usr/bin/node


const util = require('util');
const request = util.promisify(require('request'));

const fun = async () => {
  const num = process.argv.slice(2);
  if (num.length === 0) {
    return;
  }
  try {
    const url = `https://swapi-api.alx-tools.com/api/films/${num[0]}`
    let req = await request(url);
    const characters = await JSON.parse(req.body).characters;
    if (characters === undefined) {
      return;
    }
    for (let i = 0; i < characters.length; i++) {
      req = await request(characters[i]);
      const character = await JSON.parse(req.body);
      console.log(character.name);
    }
  } catch (e) {
    return e;
  }
}

fun();
