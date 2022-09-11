<h1 align="center">Data_Pipeline_VMware</h1>
<h2 align="center">Hello welcome to my README file :smiley: </h2>

I have created a web scraper that deploys to the cloud to collect an industry relevant dataset stored in a SQL database.

**Technologies used:**

**Throughout** - ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) 

**Milestone 1 & 2** - ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) 

**Milestone 3** - UUID, JSON FILE FORMAT, ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) 

**Milestone 4** - Unit testing

**Milestone 5** - ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) (RDS, S3) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) (PostgreSQL)

**Milestone 6 & 7** - ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) (RDS, S3, EC2) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

**Milestone 8** - ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

**Milestone 9** - ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) (CI/CD) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 

## Milestone 1 & 2:
* A web scraper was built 
* The website gorilla mind was chosen due to there being a lot of products available on the page to extract details from and me having some prior knowledge of the youtuber who owns the website, and so some familiarity with its  contents
* Selenium was installed and imported in order to navigate the page autonomously
* Classes were used due to the functions within the scraper sharing similar outputs and inputs
* The new scraper class finds the button for the 'all products' page, collects the link of that page, closes the sign up pop up, scrolls to the bottom of the page, collects the link for the second page from the 'next' button and then navigates to the second page
* 'if __name__=="__main__":' was used so that the function only runs if its in the correct namespace 


the code:
```python
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Scraper:
        def __init__(self):
                #constants go within the function and variables go inside the brackets above
                '''initialise'''
                self.gear_link_list = []
                self.driver = webdriver.Chrome()

        def get_website(self):
                '''navigate to website'''
                self.driver.get("https://gorillamind.com/")
                time.sleep(1)

        def collect_all_products_link(self):
                '''collect link for all products and click button to navigate to page'''
                AllProducts = self.driver.find_element(By.LINK_TEXT,"All Products")
                time.sleep(1)
                link = AllProducts.get_attribute('href')
                #collects link for all products page 1
                self.gear_link_list.append(link)
                time.sleep(2)
                AllProducts.click()
                time.sleep(10)

        def close_modal(self):
                '''closes pop up window'''
                try: 
                        modal = self.driver.find_element(By.XPATH,'//button[@class="sc-75msgg-0 RlRPc close-button cw-close"]')
                        print(modal)
                        modal.click()
                        print('Button clicked')    
                except:
                        print('No button found...exiting')
                        self.driver.quit() 
        
        def collect_next_page_link(self):
                '''scrolls to bottom of page, gets link to final page and appends to link list'''
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                next = self.driver.find_element(By.LINK_TEXT,"Next")
                link = next.get_attribute('href')
                #collects link for all products page 2
                self.gear_link_list.append(link)
                print(self.gear_link_list)
                next.click()
                time.sleep(2) 

        def main(self):
            self.get_website()
            self.collect_all_products_link()
            self.close_modal()
            self.collect_next_page_link()
            
def go_function():
    go = Scraper()
    go.main()
    pass

if __name__=="__main__":
    go_function()
           
```

## Milestone 3:
* Methods were created to retrieve key details from one of the pages, those details being: name, price, description, size, number of reviews, and the link for an image
* These methods were called extract_image and extract_text
```python
def extract_text(self):
        gear_container = self.driver.find_element(By.XPATH, '//div[@class="container"]')
        name = gear_container.find_element(By.XPATH, './/h1[@class="product_name title"]').text
        price = gear_container.find_element(By.XPATH, './/span[@class="money"]').text
        description_container= gear_container.find_element(By.XPATH, './/div[@class="description content"]')
        description = description_container.find_element(By.TAG_NAME, "p").text
        size = gear_container.find_element(By.XPATH, './/span[@class="variant-size"]').text
        num_reviews = gear_container.find_element(By.XPATH, './/a[@class="text-m"]').text
        time.sleep(2)
        ID = self.uid 
        strID = str(ID)
        print(strID)
        time.sleep(1)
        return name, price, description, size, num_reviews, strID 

def extract_image(self):
        gear_container = self.driver.find_element(By.XPATH, '//div[@class="container"]')
        image_container = gear_container.find_element(By.XPATH, './/img[@alt="Gorilla Mode"]')
        final_image  = image_container.get_attribute('data-zoom-src')
        https = 'https:'
        final_image_link = https + final_image
        time.sleep(1)
        return final_image_link
```
* The information was stored in a dictionary and a UUID was generated. UUID was used because it would generate a unique ID each time the code ran and could be used later to refer to the product dictionary saved earlier
* The information was then stored and saved locally in a folder called raw_data, the dictionary being saved as a .json file and the image being downloaded using the link in the dictionary
* A new folder was created for the product within the raw_data folder
* Within this new product folder alongside the .json file for the dictionary an images folder was created which contained the downloaded image
```python
def save_dictionary_locally(self,dict_products,strID,final_image_link):
        path = "/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/raw_data"
        os.chdir(path)
        os.makedirs(f'{strID}')
        path2 = (f"/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/raw_data/{strID}")
        os.chdir(path2)
        jsonString = json.dumps(dict_products)
        jsonFile = open("data.json", "w")
        #creates new folder for product in the 'raw_data' folder
        jsonFile.write(jsonString)
        jsonFile.close()
        
```
* The code for extracting the text, extracting the image link, downloading the image, and saving these locally were **split into individual methods in order to increase granularity** for easier reading and debugging in line with good software engineering practice. This meant that each method only dealt with one concern.
```python
   def download_image(self,strID,final_image_link):
        os.makedirs('Images')
        path3 = (f"/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/raw_data/{strID}/Images")
        os.chdir(path3)
        with open(f'{strID}_1.png', 'wb') as f:
                #downloads image in new 'Images' folder
                f.write(requests.get(final_image_link).content)
```
* the main method was also expanded in order to accomodate the new methods
![Alt text](Images/Screenshot2.png)

## Milestone 4:
* unit testing was implemeted for my web scraper script, this form of testing was selected due it being automatic and the most granular form of testing
* The methods from the script were split into public and private methods with the majority of the public methods (extract_text(), extract_image(), create_dict()) being unit tested
* A setUp and tearDown method was also implemented to test each method independantly

## Milestone 5:
* An S3 bucket was created using Amazon Web Services (AWS) and all raw data (dictionairies and image data) were uploaded to it using boto3
* An AWS Relational Database (RDS) was also created as well as a pgadmin4 database which was connected to the RDS
* The data collected from the webpage was converted to a database and cleaned using pandas:
```python 
def convert_to_pd_dataframe(self):
                df = pd.DataFrame (self.list,dtype=str)
                df['Price ($)'] = df['Price ($)'].str.strip('$')
                df['Price ($)'] = df['Price ($)'].astype('float64')
                df['Number of reviews'] = df['Number of reviews'].str.strip('Reviews')
                df['Number of reviews'] = df['Number of reviews'].astype('int64')
                return df
```
* The Price data was first stripped of any characters ($) and then converted to a float data type, this was to allow  arithmetic calculations in pgadmin4, this was also done to the 'Number of reviews' data
* The data was converted to an SQL database via sqlalchemy and psycopg2
* Using the aforemnetioned tools an engine was created that connected to pgadmin4 and by extension the RDS database:
```python
def upload_item_data_to_rds(self, df): 
                engine = create_engine(f"postgresql+psycopg2://postgres:Yoruichi786@gorilla.ctcfqngfmu8j.eu-west-2.rds.amazonaws.com:5432/Gorilla")
                df.to_sql('Products',engine,if_exists='append')
```
* The 'if_exists' attribute was set to 'append' so that values can update if they change in the future
* A method was created to notify the user that the scraper had finished saving all the data, due to the lack of shared attributes it was converted to a decorator:
```python
@staticmethod
def data_saving_update():
        print('finished saving all dictionaries and images')
```
* This was called after the data had been uploaded to the RDS, S3 bucket and saved locally:

![alt text](Images/Screenshot_4.png)

## Milestone 6 & 7:
* The RDS was checked for product data to prevent rescraping, this was acheived via the method below
```python
def check_RDS(name):
                '''
                Checks the RDS for existing files
                '''
                conn = engine.connect()
                output = conn.execute(f'''SELECT * FROM "Products" 
                                        WHERE "Name" = '{name}' ''')
                conn.close()
                check = output.fetchall()
                return check
```
* A similar method was created that checked the local directory, both of these returned values that determined whether the information from those products would be scraped
* An option was provided to the user asking whether they wanted to save locally, upload to the RDS or both
* More unittests were created to test the check_RDS method
* The scraper was changed so that it would run in headless mode by adding options to the webdriver:
```python
                options = Options()
                options.add_argument('--window-size=1920,1080')
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
                self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=options) 
```
* A docker file was made and a docker image created before being uploaded to dockerhub
![alt text](Images/Screenshot_5.png) ![alt text](Images/Screenshot_6.png) 
* An AWS EC2 instance was then created, docker was installed on the EC2 and the docker image was pulled before the scraper was run on the EC2 
![alt text](Images/Screenshot_7.png) 
* The containerisation offered by docker and the use of the AWS EC2 meant that the scraper could be run anywhere on any machine with any OS as the docker image contained all that was necessary (requirements.txt) and further pre-requisites were provided in the docker file

## Milestone 8:
* Prometheus was installed on the EC2 instance
* A prometheus.yml file was created and a docker container running prometheus was formed
```nano
global:
  scrape_interval: 15s # By default, scrape targets every 15 seconds.
  # Attach these labels to any time series or alerts when communicating with
  # external systems (federation, remote storage, Alertmanager).
  external_labels:
    monitor: 'codelab-monitor'

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name added as a label `job=<job_name>` to any timeseries scraped
  - job_name: 'prometheus'
    # Override the global default and scrape targets from job every 5 seconds.
    scrape_interval: '5s'
    static_configs:
      - targets: ['localhost:9090']
```
* A new IP address was added to the EC2 instance's inbound rules so that it's metrics could be tracked
* A daemon.json file was intialised 
```nano
{
    "metrics-addr" : "localhost:9323",
    "experimental": true,
    "features": {
    "buildkit": true
    }
}
```
* A node exporter was created to monitor the hardware of the EC2
* Two more jobs were added to the prometheus.yml file, 'node' and 'docker'. This was done so that the metrics of the docker container and EC2 could be tracked
* Docker was restarted
* Prometheus was then run on the EC2 instance using the following command 
```
sudo docker run --rm -d \
    --network=host \
    --name prometheus\
    -v /root/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus \
    --config.file=/etc/prometheus/prometheus.yml \
    --web.enable-lifecycle 
```
* The scraper was then run using the docker image
* A grafana dashboard was then set up to dispay the metrics of the EC2 instace and prometheus container
![alt text](Images/Screenshot_9.png) ![alt text](Images/Screenshot_11.png) 
* The panel directly above shows some of the hardware activity of the EC2 instance while the scraper is running
![alt text](Images/Screenshot_12.png) 
* The image above shows the status of the prometheus containers with the red line showing when the container was started
## Milestone 9:
* The steps on https://docs.docker.com/ci-cd/github-actions/ were used to add the CI/CD functionality to the project
* 2 github secrets were added, one for the dockerhub username and another for the a personal access token generated on dockerhub 
* A github workflow was created to build a docker image every time the repo was pushed to, and push it to dockerhub. This meant the image on dockerhub was always updated automatically.
![alt text](Images/Screenshot_14.png) 
* Finally a new cronjob was created on the EC2 instance to pull the new image from dockerhub, run it and then close the container everyday at a specified time
![alt text](Images/Screenshot_13.png) ![alt text](Images/Screenshot_15.png) 
<h1 align="center">Thank you for reading :smile: :blush:</h1>