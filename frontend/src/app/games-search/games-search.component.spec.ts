import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GamesSearchComponent } from './games-search.component';

describe('GamesSearchComponent', () => {
  let component: GamesSearchComponent;
  let fixture: ComponentFixture<GamesSearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GamesSearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GamesSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
