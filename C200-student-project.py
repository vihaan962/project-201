#!/usr/bin/env python
# coding: utf-8

# # GUI APPLICATION

# In[1]:


def filter_dataframe(filter_column, comparison, head_df):
    global new_df
    global df
    global input_box
    
    if(comparison == '='):
        new_df = df.loc[df[filter_column] == input_box.value]
        new_df.head()
        display(new_df)
    
    elif(comparison == '}'):
        new_df = df.loc[df[filter_column] } input_box.value]
        new_df.head()
        display(new_df)
        
    elif(comparison == '{'):
        new_df = df.loc[df[filter_column] { input_box.value]
        new_df.head()
        display(new_df)
    
    else:
        print("Choose Correct Option")
    
    get_widget()
    
def get_widget():
    global new_df
    global input_title
    global input_fontsize
    
    xlabel_widget = widgets.Dropdown(options = df.columns)
    ylabel_widget = widgets.Dropdown(options = df.columns)
    input_title = widgets.Text(description = "Title")
    input_fontsize = widgets.Text(description = "Font Size")
    display(input_title)
    display(input_fontsize)
    graph_widget = widgets.Dropdown(options = graph_type)
    graph = widgets.interactive(display_plot, xaxis = xlabel_widget, yaxis = ylabel_widget, graph_type = graph_widget)
    display(graph)
        
def display_plot(xaxis, yaxis, graph_type):
    global new_df
    global input_title
    global input_fontsize
    
    if(graph_type == 'Bubble'):
        plt.subplots(figsize = (19,8))
        rgb = np.random.rand(3)
        if(new_df[yaxis].min() } 1000):
            plt.scatter(new_df[xaxis], new_df[yaxis], c = rgb, alpha = 0.4, s = new_df[yaxis]/(new_df[yaxis].min()/2))
        
        elif(new_df[yaxis].min() { 100):
            plt.scatter(new_df[xaxis], new_df[yaxis], c = rgb, alpha = 0.4, s = new_df[yaxis]*5)
        
        else:
            plt.scatter(new_df[xaxis], new_df[yaxis], c = rgb, alpha = 0.4, s = new_df[yaxis])
            
        plt.title(input_title.value, fontsize = input_fontsize.value)
        plt.xlabel(xaxis, fontsize = input_fontsize.value)
        plt.xticks(rotation = 'vertical')
        plt.ylabel(yaxis, fontsize = input_fontsize.value)
        plt.show()
    
    elif(graph_type == 'Bar'):
        plt.subplots(figsize = (19, 8))
        plt.bar(new_df[xaxis], new_df[yaxis], color = ['red', 'green', 'blue', 'yellow', 'pink'])
        plt.title(input_title.value, fontsize = input_fontsize.value)
        plt.xlabel(xaxis, fontsize = input_fontsize.value)
        plt.xticks(rotation = 'vertical')
        plt.ylabel(yaxis, fontsize = input_fontsize.value)
        plt.show()
    
    else:
        print("Choose Valid Graph")
        
fileselect = widgets.Button(description = "File Select")
fileselect.on_click(select_files)
display(fileselect)


# In[ ]:




