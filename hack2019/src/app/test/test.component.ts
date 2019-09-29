import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss']
})
export class TestComponent implements OnInit {
  testCase: string;

  color = 'primary';
  color_max = 'warn';
  mode = 'determinate';
  value = 0;
  value_min = 100;
  value_max = 0;
  diameter = 250;

  myStyle: object = {};
  myParams: object = {};
  width: number = 100;
  height: number = 100;

  constructor(private router: Router, private http: HttpClient) {
    // Grabs last part of the url i.e. the test case
    this.testCase = window.location.href.substr(window.location.href.lastIndexOf('/') + 1);
    this.configureTest();

    let timerId = setInterval(() => this.subFunction(), 50);
  }

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

  configureTest() {
  }

  subFunction(): void {
    this.getJSON().subscribe(data => {
      if (this.testCase == "RotatorCuff" || this.testCase == "HipTwist") {
        this.value = Math.abs(data["Yaw"]) / 180 * 100;
        if (this.value_max < this.value) this.value_max = this.value;
        if (this.value_min > this.value) this.value_min = this.value;
      } else if (this.testCase == "SideLean") {
        this.value = Math.abs(data["Roll"]) / 180 * 100;
        if (this.value_max < this.value) this.value_max = this.value;
        if (this.value_min > this.value) this.value_min = this.value;
      } else {
        this.value = Math.abs(data["Pitch"]) / 180 * 100;
        if (this.value_max < this.value) this.value_max = this.value;
        if (this.value_min > this.value) this.value_min = this.value;
      }
    });
  }

  getJSON(): Observable<any> {
    return this.http.get("./assets/log.json");
  }
}
