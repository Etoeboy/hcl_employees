import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {EmployeesApiService} from './employees/employees-api.service';
import {Employee} from './employees/employee.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  employeesListSubs: Subscription;
  employeesList: Employee[];

  constructor(private employeesApi: EmployeesApiService) {
  }

  ngOnInit() {
    this.employeesListSubs = this.employeesApi
      .getEmployees()
      .subscribe(res => {
          this.employeesList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.employeesListSubs.unsubscribe();
  }
}