import LinearAlgebra.dot

normalize_vector(v::Array) = v ./ sqrt(sum(v .^ 2))
projection(v, u) = dot(v, u)u

function Gram_Schmidt(V::Array)
    U = normalize_vector.(V)
    for i in 2:length(U)
        sum_of_projections = Vector(zeros(length(U[1])))
        for j in 1:(i-1)
            sum_of_projections = sum_of_projections + projection(U[i], U[j])
        end
        U[i] = normalize_vector(U[i] - sum_of_projections)
    end
    return U
end
