import { Component, OnInit, Inject } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  testType: string = "";

  myStyle: object = {};
  myParams: object = {};
  width: number = 100;
  height: number = 100;

  constructor(private router: Router) {}

  ngOnInit() {
    this.myStyle = {
        'position': 'fixed',
        'width': '100%',
        'height': '100%',
        'z-index': -1,
        'top': 0,
        'left': 0,
        'right': 0,
        'bottom': 0,
    };

    this.myParams = {
        particles: {
            number: {
                value: 200,
            },
            color: {
                value: '#ff0000'
            },
            shape: {
                type: 'triangle',
            },
        }
    };
  }

  generateTest(event: any) {
    this.testType = event.originalTarget.innerText.replace(/\s/g, "");;
    this.router.navigate(['test/', this.testType]);
  }
}
