"use strict";

const $playedWords = $("#words");
const $form = $("#newWordForm");
const $wordInput = $("#wordInput");
const $message = $(".msg");
const $table = $("table");

let gameId;

/** Start */

async function start() {
  let response = await axios.post("/api/new-game");
  gameId = response.data.gameId;
  let board = response.data.board;

  displayBoard(board);
}

/** Display board */

function displayBoard(board) {
  $table.empty();
  // loop over board and create the DOM tr/td structure
  for (let y = 0; y < board.length; y++) {
    const $row = $("<tr>")
    for (let x = 0; x < board[0].length; x++) {
      //add coordinates to each td as a class
      const $cell = $("<td>")
      $cell.addClass(`${x}-${y}`)
      //add text to each td
      $cell.text(`${board[y][x]}`)
      $row.append($cell)
      }
    $table.append($row)
  }
}

/** Add an event handler for submits on the form */
async function handleClick(evt) {
  evt.preventDefault()

  //grab the word
  const word = $wordInput.val()

  //make a request to score the word
  let response = await axios.post("/api/score-word", {
    "gameId": gameId,
	  "word": word
  })

  const result = response.data.result

  if (result !== 'ok') {
    $message.html(result)
  } else {
    const $playedWord = $("<li></li>")
    $playedWord.html(word)
    $playedWords.append($playedWord)
  }
  debugger
}



start();
$form.on("submit", handleClick);