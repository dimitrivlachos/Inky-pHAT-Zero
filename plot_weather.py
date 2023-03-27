import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

'''
uses weather.csv to plot the weather data, plotting the temperature and humidity on the same graph
saving the graph to weather.png a 250x122 pixel image
'''

# Read data from csv file
def read_csv(filename):
    df = pd.read_csv(filename)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

# Plot data
def plot_data(df):
    dpi = 120

    x_res = 212 * 2
    y_res = 122 * 2

    # plot temperature, humidity and pressure on the same graph
    fig, ax = plt.subplots(1, 1, figsize=((x_res/dpi), (y_res/dpi)), sharex=True, dpi=dpi)
    ax.plot(df['timestamp'], df['temperature'], 'black')
    ax.plot(df['timestamp'], df['humidity'], 'black')

    # plit pressure on a second y-axis
    ax2 = ax.twinx()
    ax2.plot(df['timestamp'], df['pressure'], 'red')

    #ax.spines[['right', 'top', 'left', 'bottom']].set_visible(False)
    #ax2.spines[['right', 'top', 'left', 'bottom']].set_visible(False)

    ax.spines[['right', 'top']].set_visible(False)
    ax2.spines[['right', 'top']].set_visible(False)

    ax.set_xticks([])
    ax.set_yticks([])
    ax2.set_yticks([])

    line_thickness = 3

    # Set line width
    ax.lines[0].set_linewidth(line_thickness)
    ax.lines[1].set_linewidth(line_thickness)
    ax2.lines[0].set_linewidth(line_thickness)

    # Set xlim to the minimum and maximum values of the timestamp column
    ax.set_xlim(df['timestamp'].min(), df['timestamp'].max())

    
    
    # Save plot to file
    plt.savefig('weather.png', bbox_inches='tight', pad_inches=0)

df = read_csv('weather.csv')

# Select data only within the last 24 hours
#df = df[df['timestamp'] > pd.Timestamp.now() - pd.Timedelta('24 hours')]

plot_data(df)
