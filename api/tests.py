from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from .models import Category, Api

#test users route
class UsersTest(APITestCase):
    #create user 'testuser' and login as as 'testuser'
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        
    #test list action
    def test_users_list(self):
        get_response = self.client.get(reverse('users-list'))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertContains(get_response, self.user)
        
    #test retrieve action
    def test_users_detail(self):
        get_response = self.client.get(reverse('users-detail', args=[self.user.id]))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

#test categories route        
class CategoriesTest(APITestCase):
    #create user 'testuser' and login as as 'testuser'
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        
    #test list and create actions    
    def test_categories_list(self):
        post_response = self.client.post(reverse('categories-list'), {'name': 'weather'})
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'weather')
        
        get_response = self.client.get(reverse('categories-list'))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertContains(get_response, 'weather')
        
    #test retrieve, update, and destroy actions      
    def test_categories_detail(self):
        #create a category object to test the actions
        self.client.post(reverse('categories-list'), {'name': 'weather'})
        
        get_response = self.client.get(reverse('categories-detail', args=[Category.objects.get().id]))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertContains(get_response, 'weather')
        
        put_response = self.client.put(reverse('categories-detail', args=[Category.objects.get().id]), {'name': 'food'})
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get().name, 'food')

        
        delete_response = self.client.delete(reverse('categories-detail', args=[Category.objects.get().id]))
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)


#test apis route
class ApisTest(APITestCase):
    #create user 'testuser' and login as 'testuser'
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('categories-list'), {'name': 'food'})

    #test list and create actions
    def test_apis_list(self):
        post_response = self.client.post(reverse('apis-list'), {'name': 'Edamam Food Database Search API',
                                               'website': 'https://www.edamam.com/?gclid=Cj0KCQjw8O-VBhCpARIsACMvVLNquZKSkUXT8ibapnMJAdTd5vy841eQQgJpF5BbedFuPCRXDAqg5wYaAgJkEALw_wcB',
                                               'description': 'Get free access to a database with close to 900,000 foods and over 680,000 unique UPC codes',
                                               'category': Category.objects.get().id})
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Api.objects.get().name, 'Edamam Food Database Search API')

        
        get_response = self.client.get(reverse('apis-list'))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertContains(get_response, 'Edamam Food Database Search API')
        
    #test retrieve, update and destroy actions
    def test_apis_detail(self):
        #create an Api object to test the actions
        self.client.post(reverse('apis-list'), {'name': 'Edamam Food Database Search API',
                                               'website': 'https://developer.edamam.com/food-database-api',
                                               'description': 'Get free access to a database with close to 900,000 foods and over 680,000 unique UPC codes',
                                               'category': Category.objects.get().id})
       
        get_response = self.client.get(reverse('apis-detail', args=[Api.objects.get().id]))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertContains(get_response, 'Edamam Food Database Search API')

        put_response = self.client.put(reverse('apis-detail', args=[Api.objects.get().id]),
                                       {'name': 'Edamam Nutrition Analysis API',
                                        'website': 'https://developer.edamam.com/edamam-nutrition-api',
                                        'description': 'https://developer.edamam.com/edamam-nutrition-api',
                                        'category': Category.objects.get().id})
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(Api.objects.get().name, 'Edamam Nutrition Analysis API')

        delete_response = self.client.delete(reverse('apis-detail', args=[Api.objects.get().id]))
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Api.objects.count(), 0)


        

        
        

        
           




      
       
        

        
  
    
    
        
                                    
                                                                                        
        
        
        
        

        
       
 
    
        
    


