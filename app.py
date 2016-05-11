import alg_project3
import alg_cluster
import alg_project3_viz as viz
import alg_clusters_matplotlib

def q5():
	data_table = viz.load_data_table(viz.DATA_111_URL)
	singleton_list=[]

	for line in data_table:
		singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
	cluster_list = alg_project3.hierarchical_clustering(singleton_list, 9)
	alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)   

def q6():
	data_table = viz.load_data_table(viz.DATA_111_URL)
	singleton_list=[]
	for line in data_table:
		singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
	cluster_list = alg_project3.kmeans_clustering(singleton_list, 9, 5)
	alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)   


def compute_distortion(cluster_list, data_table):
	error = 0
	for cluster in cluster_list:
		error += cluster.cluster_error(data_table)
	return error


def q7():

	data_table = viz.load_data_table(viz.DATA_111_URL)
	singleton_list = []
	for line in data_table:
		singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

	cluster_list = alg_project3.kmeans_clustering(singleton_list, 9, 5)
	error2 = compute_distortion(cluster_list, data_table)
	
	cluster_list = alg_project3.hierarchical_clustering(singleton_list, 9)
	error1 = compute_distortion(cluster_list, data_table)

	print 'kmeans clustering', error1
	print 'hierarchical clustering',error2

def q10():
	pass

#q5()
#q6()

#q7()


q10()