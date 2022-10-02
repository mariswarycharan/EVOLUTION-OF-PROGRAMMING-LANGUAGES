from kiwisolver import UnknownConstraint
from sjvisualizer import DataHandler,Canvas,BarRace
df = DataHandler.DataHandler(excel_file="data/visual.xlsx",number_of_frames= 100*0.5*60).df
canvas = Canvas.canvas()
bar_race = BarRace.bar_race(df=df,canvas=canvas.canvas)
canvas.add_sub_plot(bar_race)
canvas.add_logo("D:\\Downloads\\Screenshot 2022-07-18 233844.png")
canvas.add_time(df=df,time_indicator='year',color=(225,0,0))
canvas.add_title('EVOLUTION OF PROGRAMMING LANGUAGES',color=(0,0,225))
canvas.add_sub_title(text="From 1990 to 2021",color=(0,255,0))
canvas.play(fps=100)







# C:\Users\USER\Documents\vs code example\work of opencv\assets

