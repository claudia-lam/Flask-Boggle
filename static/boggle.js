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

  //loop over the td
  for (let y = 0; y < board.length; y++) {
    const $row = $("<tr>")
    for (let x = 0; x < board[0].length; x++) {
      //add coordinates to each td as a class
      const $cell = $("<td>")
      $cell.addClass(`${x}-${y}`)
      $row.append($cell)
        //add text to each td
      }
    $table.append($row)
  }

}


start();