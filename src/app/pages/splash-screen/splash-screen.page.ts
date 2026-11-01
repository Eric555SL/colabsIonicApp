import { Component, OnInit, signal, } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonIcon,IonButton} from '@ionic/angular';
import { people } from 'ionicons/icons';
import { addIcons } from 'ionicons';
import { Router } from '@angular/router';

@Component({
  selector: 'app-splash-screen',
  templateUrl: './splash-screen.page.html',
  styleUrls: ['./splash-screen.page.scss'],
  imports: [IonContent, CommonModule, FormsModule, IonIcon, IonButton]
})
export class SplashScreenPage implements OnInit {
  
  constructor(private router: Router) {
    addIcons({
      'people' : people
    });
   }

  ngOnInit() {
  }
  colaboradores(){
    this.router.navigate(['/principal'])
  }

}
