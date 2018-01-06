import { Component, OnInit } from '@angular/core';
import { GamesService } from "../games.service";
import {HttpClient , HttpErrorResponse} from "@angular/common/http";

import { Game } from "../game";

const body = {
        "title": "test2",
        "description": "TestDesc2"
    };


@Component({
  selector: 'app-games',
  templateUrl: './games.component.html',
  styleUrls: ['./games.component.css']
})

export class GamesComponent implements OnInit {

  games: Game[];

  constructor(private http: HttpClient, private gamesService: GamesService) { }

  getGames(): void{
    this.gamesService.getGames()
    .subscribe(games => this.games = games);
  }

  ngOnInit(): void {
    this.getGames();

    //this.http.post('/api/v1/games/', body).subscribe();
  }

  add(title:string , desc:string ): void{
    const resp = {
      "title": title,
      "description": desc
    };
    this.http.post('/api/v1/games/', resp).subscribe();
  }

  //
  // add(title:string): void {
  // title = title.trim();
  // if (!title) { return; }
  // this.gamesService.addGame({ title } as Game)
  //   .subscribe(game => {
  //     this.games.push(game);
  //   });
  //   console.log(this.games);
  // }

  delete(game: Game): void {
    this.games = this.games.filter(h => h !== game);
    this.gamesService.deleteGame(game).subscribe();
  }

}
