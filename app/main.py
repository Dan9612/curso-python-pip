import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./data.csv')
    country = input('Ingrese pais => ')
    
    result = utils.population_by_country(data, country)
    
    if result != '':
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_charts(labels, values)
        charts.generate_pie_charts(labels, values)

if __name__ == '__main__':
    run()