export class Employee {
    constructor(
      public full_name: string,
      public phone_number: string,
      public _id?: number,
      public updatedAt?: Date,
      public createdAt?: Date,
      public lastUpdatedBy?: string,
    ) { }
  }