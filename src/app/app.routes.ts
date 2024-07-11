import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ExpenseListComponent } from './expense-list/expense-list.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'expense-list', component: ExpenseListComponent },
];
