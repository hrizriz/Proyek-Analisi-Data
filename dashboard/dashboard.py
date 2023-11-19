import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


bike_hour_df = pd.read_csv('bike_hour_df.csv', index_col=0)


average_rentals_per_day = bike_hour_df.groupby('dteday')['cnt'].mean()
average_rentals_df = average_rentals_per_day.reset_index()
average_rentals_df.columns = ['date', 'average_rentals']


total_rentals_per_hour = bike_hour_df.groupby('hr')['cnt'].sum()


bike_hour_df['dteday'] = pd.to_datetime(bike_hour_df['dteday'])

total_rentals_per_day = bike_hour_df.groupby(bike_hour_df['dteday'].dt.dayofweek)['cnt'].sum()
days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']


st.title('Rata-Rata Penyewaan Sepeda per Hari')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(average_rentals_df['date'], average_rentals_df['average_rentals'])
ax.set_title('Rata-Rata Penyewaan Sepeda per Hari')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Rata-Rata Penyewaan')
st.pyplot(fig)


st.title('Penyewa Sepeda Pada Tiap Jamnya')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(total_rentals_per_hour.index, total_rentals_per_hour.values)
ax.set_title('Sewa Sepeda Pada Tiap Jamnya')
ax.set_xlabel('Jam')
ax.set_ylabel('Total Penyewaan')
ax.set_xticks(range(0, 24))
st.pyplot(fig)


st.title('Total Penyewaan Sepeda per Hari')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(total_rentals_per_day.index, total_rentals_per_day.values, tick_label=days)
ax.set_title('Total Penyewaan Sepeda per Hari')
ax.set_xlabel('Hari')
ax.set_ylabel('Total Penyewaan')
st.pyplot(fig)
