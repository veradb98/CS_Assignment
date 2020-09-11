fix, ax = plt.subplots()
ax.plot(data.Year, data['NL Beer consumption [x1000 hectoliter]'], color = 'red', marker = 'o')
ax2 = ax.twinx()
ax2.plot(data.Year, data['WO [x1000]'], color ='blue', marker = 'o')


plt.title('Correlation between beer consumption and university students')
ax.set_xlabel("year",fontsize=14)
ax.set_ylabel("NL Beer consumption [x1000 hectoliter]",color="red",fontsize=14)
ax2.set_ylabel("WO [x1000]",color="blue",fontsize=14)

fig.savefig('Correlation between beer consumption and university students.jpg',
            format='jpeg',
            dpi=300,
            bbox_inches='tight')
            
