import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, fromEventPattern} from 'rxjs';
import 'rxjs/add/operator/catch';
import {catchError } from 'rxjs/operators';
import {API_URL} from '../env';
import {Employee} from './employee.model';

@Injectable()
export class EmployeesApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getEmployees(): Observable<any> { // Using any here for the type seems iffy, made it work though
    return this.http.request(
      'GET', `${API_URL}/employees`).pipe(
      catchError(EmployeesApiService._handleError));
  }
}