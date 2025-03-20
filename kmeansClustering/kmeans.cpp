#include <iostream>
#include <vector>
using namespace std;

int main(){
    // creating a two dimensional data points. 
    vector<vector<double>> dataPoints = {
        {1.0, 2.0},
        {1.5, 1.8},
        {5.0, 8.0},
        {8.0, 8.0},
        {1.0, 0.6},
        {9.0, 11.0},
        {8.0, 2.0},
        {10.0, 2.0},
        {9.0, 3.0}
    }; 
}


/*
#include <iostream>
#include <vector>
#include <cmath>
#include <limits>
#include <cstdlib>
#include <ctime>

// Function to calculate the Euclidean distance between two points
double euclideanDistance(const vector<double>& point1, const vector<double>& point2) {
    double sum = 0.0;
    for (size_t i = 0; i < point1.size(); ++i) {
        sum += pow(point1[i] - point2[i], 2);
    }
    return sqrt(sum);
}

// Function to initialize centroids randomly
vector<vector<double>> initializeCentroids(const vector<vector<double>>& data, int k) {
    vector<vector<double>> centroids(k);
    vector<int> usedIndexes;
    srand(time(0));
    for (int i = 0; i < k; ++i) {
        int index;
        do {
            index = rand() % data.size();
        } while (find(usedIndexes.begin(), usedIndexes.end(), index) != usedIndexes.end());
        usedIndexes.push_back(index);
        centroids[i] = data[index];
    }
    return centroids;
}

// Function to assign points to the nearest centroid
vector<int> assignClusters(const vector<vector<double>>& data, const vector<vector<double>>& centroids) {
    vector<int> clusters(data.size());
    for (size_t i = 0; i < data.size(); ++i) {
        double minDistance = numeric_limits<double>::max();
        int clusterIndex = 0;
        for (size_t j = 0; j < centroids.size(); ++j) {
            double distance = euclideanDistance(data[i], centroids[j]);
            if (distance < minDistance) {
                minDistance = distance;
                clusterIndex = j;
            }
        }
        clusters[i] = clusterIndex;
    }
    return clusters;
}

// Function to update centroids based on cluster assignments
vector<vector<double>> updateCentroids(const vector<vector<double>>& data, const vector<int>& clusters, int k) {
    vector<vector<double>> centroids(k, vector<double>(data[0].size(), 0.0));
    vector<int> counts(k, 0);
    for (size_t i = 0; i < data.size(); ++i) {
        int clusterIndex = clusters[i];
        for (size_t j = 0; j < data[i].size(); ++j) {
            centroids[clusterIndex][j] += data[i][j];
        }
        counts[clusterIndex]++;
    }
    for (int i = 0; i < k; ++i) {
        if (counts[i] > 0) {
            for (size_t j = 0; j < centroids[i].size(); ++j) {
                centroids[i][j] /= counts[i];
            }
        }
    }
    return centroids;
}

// K-means clustering algorithm
vector<int> kMeans(const vector<vector<double>>& data, int k, int maxIterations = 100) {
    vector<vector<double>> centroids = initializeCentroids(data, k);
    vector<int> clusters;
    for (int iteration = 0; iteration < maxIterations; ++iteration) {
        clusters = assignClusters(data, centroids);
        vector<vector<double>> newCentroids = updateCentroids(data, clusters, k);
        if (newCentroids == centroids) {
            break; // Stop if centroids do not change
        }
        centroids = newCentroids;
    }
    return clusters;
}

int main() {
    // Example data
    vector<vector<double>> data = {
        {1.0, 2.0},
        {1.5, 1.8},
        {5.0, 8.0},
        {8.0, 8.0},
        {1.0, 0.6},
        {9.0, 11.0},
        {8.0, 2.0},
        {10.0, 2.0},
        {9.0, 3.0}
    };

    int k = 3;
    vector<int> clusters = kMeans(data, k);

    // Output the clusters
    for (size_t i = 0; i < clusters.size(); ++i) {
        cout << "Point " << i << " is in cluster " << clusters[i] << endl;
    }

    return 0;
}

*/


