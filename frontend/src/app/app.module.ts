import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { AppRoutingModule } from './/app-routing.module';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';
import { GamesService } from './games.service';
import { GamesComponent } from './games/games.component';

// Import HttpClientModule from @angular/common/http
import {HttpClientModule} from '@angular/common/http';
import { MessageService } from './message.service';
import { MessagesComponent } from './messages/messages.component';
import { GamesSearchComponent } from './games-search/games-search.component';

@NgModule({
  declarations: [
    AppComponent,
    RegistrationComponent,
    LoginComponent,
    GamesComponent,
    MessagesComponent,
    GamesSearchComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [GamesService, MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
