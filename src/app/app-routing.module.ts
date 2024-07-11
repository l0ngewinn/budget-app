import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ExpenseListComponent } from './expense-list/expense-list.component';

const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'expense-list', component: ExpenseListComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule { }