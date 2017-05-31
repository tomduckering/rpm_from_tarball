docker build --tag rpm_builder .
docker run --volume $PWD:/spec_src rpm_builder $1
